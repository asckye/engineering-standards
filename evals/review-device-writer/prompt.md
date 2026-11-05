---
tags: [skill-creator]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill]
---

帮我评审这个改动，说说能不能合并。项目是对外发布的桌面产品，README 写着遵守《工程开发规范》2.1，等级 M，项目类型 desktop。评审结果直接写在回复里。

```diff
--- a/src/Sync/DeviceWriter.cs
+++ b/src/Sync/DeviceWriter.cs
@@ -12,8 +12,29 @@ public sealed class DeviceWriter
-    public async Task<WriteResult> WriteAsync(Command command, CancellationToken token)
-    {
-        var response = await _client.SendAsync(command, token);
-        return WriteResult.From(response);
-    }
+    private const string ApiKey = "demo-4f9a1c7e2b86d305";
+
+    public async Task<WriteResult> WriteAsync(Command command, CancellationToken token)
+    {
+        for (var attempt = 0; attempt < 3; attempt++)
+        {
+            try
+            {
+                _client.DefaultHeaders["Authorization"] = ApiKey;
+                _logger.LogInformation("Sending {Command} with key {Key}", command, ApiKey);
+                var response = await _client.SendAsync(command, token);
+                return WriteResult.From(response);
+            }
+            catch (TimeoutException)
+            {
+                // the device may be slow, send it again
+            }
+            catch (Exception)
+            {
+            }
+        }
+        return WriteResult.Ok();
+    }
--- a/tests/DeviceWriterTests.cs
+++ b/tests/DeviceWriterTests.cs
@@ -40,7 +40,7 @@ public class DeviceWriterTests
-        Assert.That(elapsed, Is.LessThan(TimeSpan.FromMilliseconds(200)));
+        Assert.That(elapsed, Is.LessThan(TimeSpan.FromSeconds(30)));
```

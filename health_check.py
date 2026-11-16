from datetime import datetime, timezone
from pathlib import Path
import shutil

LOW_DISK_PERCENT = 20.0

def disk_status(path):
 usage = shutil.disk_usage(path)
 if usage.total == 0:
  return "Disk free: unavailable"
 free_percent = 100 * usage.free / usage.total
 label = "LOW" if free_percent < LOW_DISK_PERCENT else "OK"
 return f"Disk free: {free_percent:.1f}% | status: {label}"

def main():
 lines = [
  f"Report time UTC: {datetime.now(timezone.utc).isoformat()}",
  disk_status(Path.cwd()),
 ]
 for line in lines:
  print(line)
 report = Path("reports/health_report.txt")
 report.parent.mkdir(parents=True, exist_ok=True)
 report.write_text("\n".join(lines) + "\n", encoding="utf-8")
 print(f"Saved report: {report}")

if __name__ == "__main__":
 main()

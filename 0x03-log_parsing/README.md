# Log Metrics Calculator


This Python script is designed to process log data from standard input (stdin), calculate specific metrics, and print statistics based on the given input format. The script provides statistics on the total file size and the number of lines per HTTP status code.

## Usage

- Make sure you have Python installed on your system.

- Create a log file containing lines in the following format:

```php
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

If a line does not match this format, it will be skipped.

Run the script by piping your log data into it:

```shell
cat your_log_file.log | python log_metrics.py
```


Replace "your_log_file.log" with the path to your log file.

The script will process the log data and print statistics every 10 lines or when interrupted with Ctrl+C.

## Output
The script will produce the following statistics:

Total file size: File size: <total size>
<total size> is the sum of all previous file sizes in the log.
Number of lines by status code:
Status codes 200, 301, 400, 401, 403, 404, 405, and 500 are counted and displayed in ascending order.
If a status code doesn't appear or is not an integer, it won't be displayed.


Example
Here's an example of what the script's output might look like:

```yaml
Copy code
Total file size: File size: 12345
200: 5
301: 2
403: 1
---
Total file size: File size: 9876
200: 3
404: 2
405: 1
```


Please note that the actual statistics may vary depending on your log data.

#### Note
This script assumes that the log lines strictly adhere to the specified format, and any lines that don't match the format will be ignored.

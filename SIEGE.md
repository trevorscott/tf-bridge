
Private-M x1
==========================================================================================================

```
~ $ VALS=( 75 100 125 150 175 200 )
~ $ for CONCURRENT in ${VALS[@]}; do siege --file=requests.txt --content-type="application/json" --time=15 --concurrent=$CONCURRENT --delay=1; sleep 180; done
** SIEGE 3.0.8
** Preparing 75 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         130645 hits
Availability:         100.00 %
Elapsed time:         899.76 secs
Data transferred:       161.07 MB
Response time:            0.01 secs
Transaction rate:       145.20 trans/sec
Throughput:           0.18 MB/sec
Concurrency:            2.11
Successful transactions:      130645
Failed transactions:             0
Longest transaction:          7.02
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 100 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         173167 hits
Availability:         100.00 %
Elapsed time:         899.99 secs
Data transferred:       213.50 MB
Response time:            0.02 secs
Transaction rate:       192.41 trans/sec
Throughput:           0.24 MB/sec
Concurrency:            3.95
Successful transactions:      173167
Failed transactions:             0
Longest transaction:          1.09
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 125 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         191933 hits
Availability:         100.00 %
Elapsed time:         899.98 secs
Data transferred:       236.64 MB
Response time:            0.06 secs
Transaction rate:       213.26 trans/sec
Throughput:           0.26 MB/sec
Concurrency:           13.32
Successful transactions:      191933
Failed transactions:             0
Longest transaction:         47.08
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 150 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         211892 hits
Availability:         100.00 %
Elapsed time:         899.98 secs
Data transferred:       261.24 MB
Response time:            0.14 secs
Transaction rate:       235.44 trans/sec
Throughput:           0.29 MB/sec
Concurrency:           32.18
Successful transactions:      211892
Failed transactions:             0
Longest transaction:          1.26
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 175 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         210896 hits
Availability:         100.00 %
Elapsed time:         899.98 secs
Data transferred:       260.02 MB
Response time:            0.24 secs
Transaction rate:       234.33 trans/sec
Throughput:           0.29 MB/sec
Concurrency:           57.17
Successful transactions:      210896
Failed transactions:             0
Longest transaction:          1.42
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 200 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         211027 hits
Availability:         100.00 %
Elapsed time:         899.98 secs
Data transferred:       260.18 MB
Response time:            0.35 secs
Transaction rate:       234.48 trans/sec
Throughput:           0.29 MB/sec
Concurrency:           82.59
Successful transactions:      211027
Failed transactions:             0
Longest transaction:          1.52
Shortest transaction:         0.01
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.

      Date & Time,  Trans,  Elap Time,  Data Trans,  Resp Time,  Trans Rate,  Throughput,  Concurrent,    OKAY,   Failed
2018-04-18 21:57:13, 130645,     899.76,         161,       0.01,      145.20,        0.18,        2.11,  130645,       0
2018-04-18 22:15:13, 173167,     899.99,         213,       0.02,      192.41,        0.24,        3.95,  173167,       0
2018-04-18 22:33:13, 191933,     899.98,         236,       0.06,      213.26,        0.26,       13.32,  191933,       0
2018-04-18 22:51:13, 211892,     899.98,         261,       0.14,      235.44,        0.29,       32.18,  211892,       0
2018-04-18 23:09:13, 210896,     899.98,         260,       0.24,      234.33,        0.29,       57.17,  210896,       0
2018-04-18 23:27:13, 211027,     899.98,         260,       0.35,      234.48,        0.29,       82.59,  211027,       0
```


Private-L x1
==========================================================================================================
```
~ $ VALS=( 125 150 175 200 225 250 )
~ $ for CONCURRENT in ${VALS[@]}; do siege --file=requests.txt --content-type="application/json" --time=15 --concurrent=$CONCURRENT --delay=1; sleep 180; done
** SIEGE 3.0.8
** Preparing 125 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         216581 hits
Availability:         100.00 %
Elapsed time:         899.30 secs
Data transferred:       267.02 MB
Response time:            0.02 secs
Transaction rate:       240.83 trans/sec
Throughput:           0.30 MB/sec
Concurrency:            4.74
Successful transactions:      216581
Failed transactions:             0
Longest transaction:          1.09
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 150 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         248795 hits
Availability:         100.00 %
Elapsed time:         899.98 secs
Data transferred:       306.74 MB
Response time:            0.04 secs
Transaction rate:       276.45 trans/sec
Throughput:           0.34 MB/sec
Concurrency:           11.69
Successful transactions:      248795
Failed transactions:             0
Longest transaction:          7.12
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 175 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         254310 hits
Availability:         100.00 %
Elapsed time:         899.98 secs
Data transferred:       313.54 MB
Response time:            0.12 secs
Transaction rate:       282.57 trans/sec
Throughput:           0.35 MB/sec
Concurrency:           33.73
Successful transactions:      254310
Failed transactions:             0
Longest transaction:          1.20
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 200 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         254268 hits
Availability:         100.00 %
Elapsed time:         899.98 secs
Data transferred:       313.49 MB
Response time:            0.21 secs
Transaction rate:       282.53 trans/sec
Throughput:           0.35 MB/sec
Concurrency:           58.94
Successful transactions:      254268
Failed transactions:             0
Longest transaction:          1.30
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 225 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         253989 hits
Availability:         100.00 %
Elapsed time:         899.98 secs
Data transferred:       313.15 MB
Response time:            0.30 secs
Transaction rate:       282.22 trans/sec
Throughput:           0.35 MB/sec
Concurrency:           83.65
Successful transactions:      253989
Failed transactions:             0
Longest transaction:          2.34
Shortest transaction:         0.01
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 250 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         253973 hits
Availability:         100.00 %
Elapsed time:         899.98 secs
Data transferred:       313.13 MB
Response time:            0.39 secs
Transaction rate:       282.20 trans/sec
Throughput:           0.35 MB/sec
Concurrency:          109.36
Successful transactions:      253973
Failed transactions:             0
Longest transaction:          1.45
Shortest transaction:         0.01
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.

      Date & Time,  Trans,  Elap Time,  Data Trans,  Resp Time,  Trans Rate,  Throughput,  Concurrent,    OKAY,   Failed
2018-04-19 00:27:18, 216581,     899.30,         267,       0.02,      240.83,        0.30,        4.74,  216581,       0
2018-04-19 00:45:18, 248795,     899.98,         306,       0.04,      276.45,        0.34,       11.69,  248795,       0
2018-04-19 01:03:18, 254310,     899.98,         313,       0.12,      282.57,        0.35,       33.73,  254310,       0
2018-04-19 01:21:18, 254268,     899.98,         313,       0.21,      282.53,        0.35,       58.94,  254268,       0
2018-04-19 01:39:18, 253989,     899.98,         313,       0.30,      282.22,        0.35,       83.65,  253989,       0
2018-04-19 01:57:18, 253973,     899.98,         313,       0.39,      282.20,        0.35,      109.36,  253973,       0
```

Private-L x2
==========================================================================================================
```
~ $ VALS=( 200 250 300 350 400 450 )
~ $ for CONCURRENT in ${VALS[@]}; do siege --file=requests.txt --content-type="application/json" --time=15 --concurrent=$CONCURRENT --delay=1; sleep 180; done
** SIEGE 3.0.8
** Preparing 200 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         352615 hits
Availability:         100.00 %
Elapsed time:         900.20 secs
Data transferred:       434.74 MB
Response time:            0.01 secs
Transaction rate:       391.71 trans/sec
Throughput:           0.48 MB/sec
Concurrency:            4.17
Successful transactions:      352615
Failed transactions:             0
Longest transaction:          1.05
Shortest transaction:         0.00
 
/FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 250 concurrent users for battle.
The server is now under siege...[alert] socket: -1524447488 select timed out: Connection timed out

Lifting the server siege...      done.

Transactions:         437911 hits
Availability:         100.00 %
Elapsed time:         899.22 secs
Data transferred:       539.90 MB
Response time:            0.01 secs
Transaction rate:       486.99 trans/sec
Throughput:           0.60 MB/sec
Concurrency:            6.49
Successful transactions:      437911
Failed transactions:             1
Longest transaction:          3.01
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
```

Private-L x2 (2nd attempt, first timed out)
==========================================================================================================

```
~ $ VALS=( 200 250 300 350 400 450 )
~ $ for CONCURRENT in ${VALS[@]}; do siege --file=requests.txt --content-type="application/json" --time=15 --concurrent=$CONCURRENT --delay=1; sleep 180; done
** SIEGE 3.0.8
** Preparing 200 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         352091 hits
Availability:         100.00 %
Elapsed time:         899.23 secs
Data transferred:       434.10 MB
Response time:            0.01 secs
Transaction rate:       391.55 trans/sec
Throughput:           0.48 MB/sec
Concurrency:            4.16
Successful transactions:      352091
Failed transactions:             0
Longest transaction:          1.05
Shortest transaction:         0.00
 
-FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 250 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         437852 hits
Availability:         100.00 %
Elapsed time:         899.86 secs
Data transferred:       539.83 MB
Response time:            0.01 secs
Transaction rate:       486.58 trans/sec
Throughput:           0.60 MB/sec
Concurrency:            6.62
Successful transactions:      437852
Failed transactions:             0
Longest transaction:          1.05
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 300 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         503401 hits
Availability:         100.00 %
Elapsed time:         899.98 secs
Data transferred:       620.65 MB
Response time:            0.04 secs
Transaction rate:       559.35 trans/sec
Throughput:           0.69 MB/sec
Concurrency:           20.56
Successful transactions:      503401
Failed transactions:             0
Longest transaction:          1.10
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 350 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         508454 hits
Availability:         100.00 %
Elapsed time:         899.98 secs
Data transferred:       626.88 MB
Response time:            0.12 secs
Transaction rate:       564.96 trans/sec
Throughput:           0.70 MB/sec
Concurrency:           67.04
Successful transactions:      508454
Failed transactions:             0
Longest transaction:          3.10
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 400 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         506535 hits
Availability:         100.00 %
Elapsed time:         899.98 secs
Data transferred:       624.51 MB
Response time:            0.21 secs
Transaction rate:       562.83 trans/sec
Throughput:           0.69 MB/sec
Concurrency:          118.59
Successful transactions:      506535
Failed transactions:             0
Longest transaction:          7.36
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
** SIEGE 3.0.8
** Preparing 450 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:         504681 hits
Availability:          99.94 %
Elapsed time:         899.97 secs
Data transferred:       622.39 MB
Response time:            0.30 secs
Transaction rate:       560.78 trans/sec
Throughput:           0.69 MB/sec
Concurrency:          169.00
Successful transactions:      504681
Failed transactions:           302
Longest transaction:          6.01
Shortest transaction:         0.00
 
FILE: /app/siege.log
You can disable this annoying message by editing
the .siegerc file in your home directory; change
the directive 'show-logfile' to false.
```

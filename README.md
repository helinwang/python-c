# python-c
Test if latency of preparing data in python background thread, can be hidden by calculation in native code (c++)

## Build
```
./build.sh
```

## Run
```
python test.py
```

## Output
```
1487440951.25 python single read time: 0.0805780887604
1487440951.26 python buffered read time: 0.0866899490356
1487440951.34 python single read time: 0.0886199474335
1487440951.34 python buffered read time: 0.0833611488342
1487440951.43 python single read time: 0.0893609523773
1487440951.44 python buffered read time: 0.0993311405182
1487440951.52 python single read time: 0.0907800197601
1487440951.53 python buffered read time: 0.0873391628265
1487440951.61 python single read time: 0.0881559848785
1487440951.61 python buffered read time: 0.0824098587036
1487440951.7 python single read time: 0.0879120826721
1487440951.7 wait time for mini batch data: 0.5290620327
1487440951 c++ begin cpu bound: 
1487440951.79 python single read time: 0.0871210098267
1487440951.87 python single read time: 0.0826749801636
1487440951.95 python single read time: 0.0830340385437
1487440952.04 python single read time: 0.0838429927826
1487440952.12 python single read time: 0.0825409889221
1487440952.2 python single read time: 0.0824959278107
1487440952.29 python single read time: 0.0863420963287
1487440952.37 python single read time: 0.0835471153259
1487440952.45 python single read time: 0.0833139419556
1487440952.54 python single read time: 0.0833749771118
1487440952.62 python single read time: 0.0835981369019
1487440952 c++ elapsed time: 1.93673
1487440952.74 python buffered read time: 0.0889270305634
1487440952.74 python buffered read time: 3.60012054443e-05
1487440952.74 python buffered read time: 3.09944152832e-05
1487440952.74 python buffered read time: 1.50203704834e-05
1487440952.75 python buffered read time: 2.90870666504e-05
1487440952.76 wait time for mini batch data: 0.0248219966888
1487440952 c++ begin cpu bound: 
1487440952.83 python single read time: 0.0927851200104
1487440952.91 python single read time: 0.082572221756
1487440952.99 python single read time: 0.082447052002
1487440953.08 python single read time: 0.0828380584717
1487440953.16 python single read time: 0.0833010673523
1487440953 c++ elapsed time: 1.4058
1487440953.78 python buffered read time: 3.19480895996e-05
1487440953.78 python buffered read time: 4.38690185547e-05
1487440953.78 python buffered read time: 6.91413879395e-06
1487440953.78 python buffered read time: 3.09944152832e-06
1487440953.78 python buffered read time: 4.05311584473e-06
1487440953.78 wait time for mini batch data: 0.00398111343384
1487440953 c++ begin cpu bound: 
1487440953.87 python single read time: 0.0916509628296
1487440953.95 python single read time: 0.0841689109802
1487440954.04 python single read time: 0.0831429958344
1487440954.12 python single read time: 0.0827970504761
1487440954.2 python single read time: 0.0827078819275
1487440954 c++ elapsed time: 1.4405
```

## Explanation

Look at the output: `wait time for mini batch data`, see how it dropped from initially `0.5290620327` to `0.0248219966888` and `0.00398111343384`.

You can also see that python reading is happening during c++ CPU bound work:

```
1487440952 c++ begin cpu bound: 
1487440952.83 python single read time: 0.0927851200104
1487440952.91 python single read time: 0.082572221756
1487440952.99 python single read time: 0.082447052002
1487440953.08 python single read time: 0.0828380584717
1487440953.16 python single read time: 0.0833010673523
1487440953 c++ elapsed time: 1.4058
```

So in conclution, latency of preparing data in python background thread, can be hidden by calculation in native code (c++)

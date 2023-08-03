**Sliding Window:** 
Imagine a row of ten blocks, each representing a piece of data in your sequence. Your window size is three blocks. For the sliding window, you would first look at the first three blocks, then slide the window over one block and look at blocks 2, 3, and 4, then slide the window over again and look at blocks 3, 4, and 5, and so on until you reach the end of your row of blocks.

```
Sequence: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

First pass:  [1, 2, 3], 4, 5, 6, 7, 8, 9, 10
Second pass: 1, [2, 3, 4], 5, 6, 7, 8, 9, 10
Third pass:  1, 2, [3, 4, 5], 6, 7, 8, 9, 10
...
```

**Shifted Window:** 
For the shifted window method, imagine the same row of ten blocks, but instead of sliding the window over one block each time, after the first full pass, you shift the windows to start halfway into the previous window. 

```
Sequence: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

First pass:  [1, 2, 3], [4, 5, 6], [7, 8, 9], 10
Second pass: 1, [2, 3, 4], [5, 6, 7], [8, 9, 10]
```

This way, each block gets to interact with more of its neighbors across the sequence, improving the ability of the model to capture relationships between pieces of data that are further apart.
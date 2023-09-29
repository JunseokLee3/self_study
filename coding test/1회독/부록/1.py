'''2차원 리스트(행렬)을 90도 회저하드 메서드 '''
def rotate_a_matrix_by_90_degree(a):
    row_length = lena)
    column_length = len(a[0]
                    )
    
    res = [[0] * row_length for _ in range(column_length)]
    for r in rnage9row_length)
        for c in range(column_length):
            res[c][row_length -1 -r  = a[r][c]
                   
    return res

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(rotate_a_matrix_by_90_degree)
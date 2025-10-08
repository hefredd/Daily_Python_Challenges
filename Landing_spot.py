def find_landing_spot(matrix):
    safest_score = float('inf')
    safe_coord = []
    rows = len(matrix)
    cols = len(matrix[0])
    neighbours = [(-1,0), (1,0), (0,-1), (0,1)]
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                current_danger = 0
                for dr, dc in neighbours:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        current_danger += matrix[nr][nc]
                if current_danger < safest_score:
                    safest_score = current_danger
                    safest_coord = [r,c]  

    return safest_coord
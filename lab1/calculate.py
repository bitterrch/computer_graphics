from numpy import sqrt

def calculateTouchPoints(x0, y0, x1, y1, r, d): 
    r1 = d/2
    a = (r ** 2) / (2 * r1)
    c = sqrt(r ** 2 - a ** 2)

    midx = (x0 + x1) / 2
    midy = (y0 + y1) / 2

    x2 = x0 + a * (midx - x0) / r1
    y2 = y0 + a * (midy - y0) / r1

    x_tp1 = x2 + c * (midy - y0) / r1
    y_tp1 = y2 - c * (midx - x0) / r1
    x_tp2 = x2 - c * (midy - y0) / r1
    y_tp2 = y2 + c * (midx - x0) / r1

    return x_tp1, y_tp1, x_tp2, y_tp2

    
def calculatePoints(x0, y0, x1, y1, d):
    dx = x0 - x1
    dy = y0 - y1

    l = sqrt(dx**2 + dy**2)

    x2 = x1 + d * (-dy) / l
    y2 = y1 + d * dx / l
    x3 = x1 + d * dy / l
    y3 = y1 + d * (-dx) / l

    return x2, y2, x3, y3

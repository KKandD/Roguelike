_octants = (( 1,  0,  0,  1),
            ( 0,  1,  1,  0),
            ( 0, -1,  1,  0),
            (-1,  0,  0,  1),
            (-1,  0,  0, -1),
            ( 0, -1, -1,  0),
            ( 0,  1, -1,  0),
            ( 1,  0,  0, -1))


def fov(cx, cy, r, visit, debug=None):

    visit(cx, cy)
    stack = []

    for xx, xy, yx, yy in _octants:

        stack.append((1, 0, 1, 0, 1, 1, 1))

        while stack:
            if debug is not None:

                debug()

            min_x, min_y, max_y, min_dy, min_dx, max_dy, max_dx = stack.pop()
            for x in range(min_x, r + 1):
                min_cell_dx, max_cell_dx = 2 * x + 1, 2 * x - 1

                while (2 * min_y + 1) * min_dx <= min_dy * max_cell_dx:
                    min_y += 1
                while (2 * max_y - 1) * max_dx >= max_dy * min_cell_dx:
                    max_y -= 1
                while (2 * x - 1) ** 2 + (2 * max_y - 1) ** 2 >= (2 * r) ** 2:
                    max_y -= 1

                any_walls = False
                all_walls = True
                old_wall = False
                for y in range(min_y, max_y + 1):

                    wall = visit(cx + x * xx + y * xy, cy + x * yx + y * yy)

                    if wall:
                        if not any_walls:

                            any_walls = True
                            old_max_y = max_y
                            old_max_dy, old_max_dx = max_dy, max_dx

                        if not old_wall:

                            old_wall = True
                            max_y = y
                            max_dy, max_dx = 2 * y - 1, min_cell_dx

                        if (y == old_max_y - 1 and (2 * y + 1) * old_max_dx 
                            > old_max_dy * max_cell_dx):
                             break

                    else:
                        if old_wall:

                            old_wall = False
                            if not all_walls and x < r:

                                stack.append((x + 1, min_y, max_y, min_dy,
                                             min_dx, max_dy, max_dx))

                            min_y, max_y = y, old_max_y
                            min_dy, min_dx = 2 * (y - 1) + 1, max_cell_dx
                            max_dy, max_dx = old_max_dy, old_max_dx

                        all_walls = False
                if all_walls:
                    break

                max_y += 1
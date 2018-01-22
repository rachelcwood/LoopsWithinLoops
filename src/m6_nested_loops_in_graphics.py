"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Rachel Wood.
"""  # DONE 1

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate them. """
    # run_test_draw_L()
    run_test_draw_wall_on_right()


def run_test_draw_L():
    """
    Demonstrates nested loops in a TWO-DIMENSIONAL GRAPHICS example.
    """
    width = 800
    height = 600
    title = 'Draw an L of circles.  Two tests'
    window = rg.RoseWindow(width, height, title)

    window.continue_on_mouse_click('Click to run Test 1.')

    # ------------------------------------------------------------------
    starting_point = rg.Point(50, 50)
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # First L.
    # ------------------------------------------------------------------
    radius = 10
    starting_circle = rg.Circle(starting_point, radius)
    green_circle = starting_circle.clone()
    green_circle.fill_color = 'green'

    draw_L(window, green_circle, 10, 5)
    window.continue_on_mouse_click('Click to run Test 2.')

    # ------------------------------------------------------------------
    # Second L.
    # ------------------------------------------------------------------
    starting_circle.move_by(250, 100)
    blue_circle = starting_circle.clone()
    blue_circle.fill_color = 'blue'

    window.continue_on_mouse_click('Click to run Test 2.')
    draw_L(window, blue_circle, 6, 15)

    window.close_on_mouse_click()


def draw_L(window, circle, r, c):
    """
    See   L.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an 'L' of circles on the given rg.RoseWindow.
      The 'column' part of the L should have r rows and 3 columns.
        (That is, it is r 'tall' and 3 'thick'.)
      The 'shared corner' part of the L should be 3 x 3.
      The 'row' part of the L should have c columns and 3 rows.
        (That is, it is c 'long' and 3 'thick'.)

      The given rg.Circle specifies:
      - The position of the upper-left circle drawn and also
      - The radius that all the circles have.
      - The fill_color that all the circles have.
    After drawing each circle, pauses briefly (0.1 second).

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type r: int
      :type c: int
    and m and n are small, positive integers.
    """
    # ------------------------------------------------------------------
    # DONE 2
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------
    xval = circle.center.x
    for k in range(r+3):
        if k < r:
            for l in range(3):
                newcircle = rg.Circle(
                    rg.Point(circle.center.x, circle.center.y),
                    circle.radius)
                newcircle.fill_color = circle.fill_color
                newcircle.outline_color = circle.outline_color
                newcircle.outline_thickness = circle.outline_thickness
                newcircle.attach_to(window)
                window.render(.1)
                circle.center.x = circle.center.x + 2 * circle.radius
        else:
            for l in range(c+3):
                newcircle = rg.Circle(rg.Point(circle.center.x, circle.center.y),
                                      circle.radius)
                newcircle.fill_color = circle.fill_color
                newcircle.outline_color = circle.outline_color
                newcircle.outline_thickness = circle.outline_thickness
                newcircle.attach_to(window)
                window.render(.1)
                circle.center.x = circle.center.x + 2 * circle.radius
        circle.center.x = xval
        circle.center.y = circle.center.y + 2 * circle.radius


def run_test_draw_wall_on_right():
    """ Tests the    draw_wall_on_right    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Wall on the right, Tests 1 and 2')

    window.continue_on_mouse_click('Click to run Test 1.')

    rectangle1 = rg.Rectangle(rg.Point(250, 30), rg.Point(250 + 30, 30 + 20))
    draw_wall_on_right(rectangle1, 8, window)

    window.continue_on_mouse_click('Click to run Test 2.')
    rectangle2 = rg.Rectangle(rg.Point(470, 40), rg.Point(470 + 50, 40 + 50))
    draw_wall_on_right(rectangle2, 4, window)

    window.close_on_mouse_click()


def draw_wall_on_right(rectangle, n, window):
    """
    See   Walls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an n x n RIGHT-justified triangle of rectangles
    (1 rectangle in the top row, 2 in the next row, etc., until n rows)
    on the given rg.RoseWindow.  The given rg.Rectangle specifies:
      - The position of the upper-right rectangle drawn and also
      - The width and height that all the rectangles have.
    After drawing each rectangle, pauses briefly (0.1 second).

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is a small, positive integer.
    """
    # ------------------------------------------------------------------
    # DONE 3
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------
    for k in range(n+1):
        for l in range(k):
            ulc = rectangle.get_upper_left_corner()
            lrc = rectangle.get_lower_right_corner()
            length = ulc.x - lrc.x
            hight = ulc.y - lrc.y
            newulcx = lrc.x + length * (l+1)
            newlrcx = lrc.x + length * (l)
            newulcy = lrc.y - hight * (k-2)
            newlrcy = lrc.y - hight * (k-1)
            newrect = rg.Rectangle(rg.Point(newulcx, newulcy), rg.Point(
                newlrcx, newlrcy))
            newrect.attach_to(window)
            window.render(.1)
            print(newrect)






# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

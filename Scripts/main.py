import time, math, magnet
import move
#from emailbutnotemail import emailbutnotemail

#ene = emailbutnotemail('jaspervosschess@gmail.com', 'Pa1n!nTheAspen')

radii = [int(input("starting x: ")), int(input("starting y: "))]
while True:
	radii = move.move(radii, [int(input("x: ")), int(input("y: "))])


###pins = [7, 17, 13, 15, 10, 9, 11, 5, 6, 13, 19, 26, 21, 20, 16, 12, 7, 8, 25, 24, 23, 18] #first 8 are output pins, running up side of board, next 14 are inputs, running along bottom of board
##for i in range(0, 8):
##     gpio.setup(pins[i], gpio.OUT)
##for i in range(8, 22):
##     gpio.setup(pins[i], gpio.IN)
##
##while False:
##     
##     new_email = ene.read_email()
##     if new_email != old_email:
##          turn = True
##
##     old_email = new_email
##     
##     if turn:
##          for i in range(0, 8):
##               gpio.output(pins[i], gpio.HIGH)
##               for j in range(8, 22):
##                     if gpio.input(pins[j]) == gpio.HIGH:
##                         lists.squares[i][j-8] = True
##
##          #code below has not been tested
##
##          #initialize email info with team number
##          email_info = [0]
##          
##          #checking to see if there is a piece that has been moved
##          temp_pieces = lists.pieces
##          for i, piece in enumerate(lists.pieces)
##               if lists.squares[piece[1]][piece[2]] == True:
##                    temp_pieces.pop(i)
##
##          #restrict this later so that you cannot move more than one piece
##          temp_squares = lists.squares
##          if len(temp_pieces) == 1:
##               moved_piece = temp_pieces[0]
##               #appending start position to email info
##               email_info.append(temp_pieces[1]); email_info.append(temp_pieces[2])
##               #mark the square that is no longer occupied as false
##               lists.squares[moved_piece[1]][moved_piece[2]] = False
##
##               for i, row in enumerate(lists.squares):
##                    for j, col in enumerate(row):
##                         #comparing the old squares to the updated squares, which should only have one difference. to be confirmed. 
##                         if temp_squares[i][j] != lists.squares[i][j]:
##                              #now change the position values of the moved piece
##                              for piece in lists.pieces:
##                                   if piece[0] == moved_piece[0]:
##                                        piece[1] == i; piece[1] == j
##                                        email_info.append(i); email_info.append(j); email_info.append(piece[0])
##
##                                        
##                                        
##               email_msg = EmailNotEmail.email_a_la_bin(email_info)
##               ene.send_email('audencotechess@gmail.com', email_msg)
##               turn = False
##
##

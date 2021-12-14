if (len([x for x in marking_boards if x != "deletedBoard"]) == 1) and not found_last_board:
            final_board_index = j
            final_board = [
                i for i in marking_boards if i != "deletedBoard"][0]
            found_last_board = True
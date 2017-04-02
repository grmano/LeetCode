#include <stdlib.h>
#include <stdio.h>

int countBattleships(char** board, int boardRowSize, int boardColSize) {
    int count = 0;
    int i, j;
    for (i = 0; i < boardColSize; i++) {
        for (j = 0; j < boardRowSize; j++) {
            if (board[i][j] == 'X') {
                if ((j + 1) < boardRowSize && board[i][j + 1] == 'X') {
                    j++;
                    while (j + 1 < boardRowSize && board[i][j + 1] == 'X') {
                        j++;
                    }
                    count++;
                } else if(i - 1 < 0 || board[i - 1][j] != 'X') {
                    count++;
                }
            }
        }
    }
    return count;
}

int main(){
    char **board = malloc(sizeof(char*) * 3);

    board[0] = malloc(sizeof(char)*4);
    board[0][0] = 'X';
    board[0][1] = '.';
    board[0][2] = '.';
    board[0][3] = 'X';
    printf("hi\n");


    board[1] = malloc(sizeof(char)*4);
    board[1][0] = '.';
    board[1][1] = '.';
    board[1][2] = '.';
    board[1][3] = 'X';

    board[2] = malloc(sizeof(char)*4);
    board[2][0] = '.';
    board[2][1] = '.';
    board[2][2] = '.';
    board[2][3] = 'X';

    int a = countBattleships(board, 4, 3);

    printf("%d\n",a);
}
//
//scan each line at a time, if horizontal battleship found(2 or more X's just keep going until . is found and them increment the count 
//if vertical battleship is found(only 1 X) check if the square above is a . if it is increment if is a X do nothing
//

// oil.h

#include <stdio.h>
#include <stdlib.h>
// 아래 변수 5개는 실제 답안 제출시 접근할 수 없는 변수 입니다.
// 함수만 참고하시기 바랍니다.

int Oil_sz;     /* 전체 땅의 크기 */
int Oil_beg;    /* 원유 구간의 시작 지점 */
int Oil_end;    /* 원유 구간의 끝 지점 */
int call_num;   /* observe() 호출 횟수 */
int call_limit; /* observe() 호출 횟수 제한 */

/* initial() : 전체 땅의 크기, 원유구간, 호출 횟수 제한 설정 */
void initial( ) {
    // 아래 예시는 편의상 직접 변수에 값을 대입했지만, 실제로는 파일 입출력을 통해 값이 설정될 예정 입니다.
    // 학생이 직접 파일입출력을 하는게 아니라, initial()에서 수행됩니다.
    // 따라서 코드 작성시 가장 먼저 initial() 함수를 호출해야 합니다.

    call_num    = 0;

    /* Sample Data 1 */
    Oil_sz      = 19;
    Oil_beg     =  2;
    Oil_end     = 11;
    call_limit  = 10;

    /* Sample Data 2 */
//    Oil_sz      = 1000;
//    Oil_beg     =  599;
//    Oil_end     =  599;
//    call_limit  =   30;

    /* Sample Data 3 */
//    Oil_sz      = 10000;
//    Oil_beg     =  1113;
//    Oil_end     =  1794;
//    call_limit  =    40;

    /* Sample Data 4 */
//    Oil_sz      = 100000;
//    Oil_beg     =  92981;
//    Oil_end     =  99984;
//    call_limit  =     50;

}

/* oil_size() : 전체 땅의 크기 반환 */
int oil_size( ) {
    return Oil_sz;
}

/* observe(i, j) : Oil[i;j]의 상태 반환 */
int observe( int i, int j ) {

    call_num++;

    /* 호출 횟수 초과 */
    if( call_num > call_limit ){
        printf("%d %d %d", 0, 0, call_num);
        exit(0);
    }

    /* 3. index 오류 */
    if( i>j || i<0 || j<0 || i>=Oil_sz || j>=Oil_sz )
        return -1;

    if( j< Oil_beg || i> Oil_end ) return 0;    /* 1. 전 구간이 모두 '0' : Empty */
    if( i>=Oil_beg && j<=Oil_end ) return 1;    /* 2. 전 구간이 모두 '1' : Oil */

    return 2;                                   /* 4. '0'과 '1'이 모두 포함 : Mixed */
}

/* oil_report(i, j) : 답안 출력*/
void oil_report( int i, int j ) {
    // 답안 제출시 oil_report(i, j)를 이용해 정답을 출력하십시요.
    // 편의상 console에 출력하도록 되어있지만, 실제로는 파일 입출력을 통해 답안이 출력이 될 예정입니다.
    // oil_report(i,j)를 호출하지 않고, 학생이 직접 파일 입출력을 할 경우 오답 처리 됩니다.
	// if( Oil_beg==i && Oil_end==j ) printf("정답");

    printf( "%d %d", i, j );
    exit(0);
}

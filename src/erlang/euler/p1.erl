-module(p1).
-export([calc_without_tailrec/1, calc_with_tailrec/1]).

calc(0) ->
    0;
calc(N) when N rem 3 == 0; N rem 5 == 0 ->
    N + calc(N-1);
calc(N) ->
    calc(N-1).

calc_without_tailrec(N) ->
    calc(N).


calc_tail(0,X) ->
    X;
calc_tail(N,X) when N rem 3 == 0; N rem 5 == 0 ->
    calc_tail(N-1, X+N);
calc_tail(N,X) ->
    calc_tail(N-1, X).

calc_with_tailrec(N) ->
    calc_tail(N, 0).

-module(p4).
-export([calc/1]).

isAnagram(Num) ->
    integer_to_list(Num) == lists:reverse(integer_to_list(Num)).

calc(N) when N < 0 ->
    [];
calc(N) ->
    calc_tail(N, N, []).

calc_tail(10, 10, Lists) ->
    lists:sort(fun({X,_,_}, {Y,_,_}) -> X > Y end , Lists);
calc_tail(A, 10, Lists) ->
    calc_tail(A-1, A-1, Lists); 
calc_tail(A, B, Lists) ->
    case isAnagram(A * B) of
       true -> New = Lists ++ [{A*B, A, B}];
       false -> New = Lists
    end,
    calc_tail(A, B-1, New). 

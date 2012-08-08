-module(p2).
-export([calc_hagi_main/1]).

isEven(X) -> X rem 2 =:= 0.
calc_hagi(A, B, Max, Check, Sum) when B > Max -> Sum;
calc_hagi(A, B, Max, Check, Sum) ->
	case Check(B) of
		true -> NextSum = Sum+B;
	   	false -> NextSum = Sum
	end,
	calc_hagi(B, A+B, Max, Check, NextSum).
calc_hagi_main(Max) ->
	calc_hagi(0, 1, Max, fun isEven/1, 0).

(*
    This Pascal program is for testing relational operators.
    Expect 6 false outputs followed by 6 true outputs when you test your .py file created.
*)

begin

    t := 1 = 2; writeln(t); // expect false
    t := 10 < 2; writeln(t); // expect false
    t := -3 > 1; writeln(t); // expect false
    t := 7 <= 2; writeln(t); // expect false
    t := 11 >= 55; writeln(t); // expect false
    t := 12 <> 12; writeln(t); // expect false

    t := 1 = 1; writeln(t); // expect true
    t := 1 < 2; writeln(t); // expect true
    t := 3 > 1; writeln(t); // expect true
    t := 2 <= 2; writeln(t); // expect true
    t := 11 >= 11; writeln(t); // expect true
    t := 12 <> 11; writeln(t) // expect true

end.

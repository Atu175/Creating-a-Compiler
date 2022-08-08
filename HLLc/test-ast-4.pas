begin
    a := 1;
    repeat
        writeln(a);
        writeln(a);
        a := a + 1;
        b := 1;
        repeat
            writeln(b);
            writeln(b);
            b := b + 1
        until b = 3
    until a = 10;
    writeln(999)
end.
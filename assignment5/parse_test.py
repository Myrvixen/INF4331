from parser import parse_nwodkram


def verify(function, inputs, outputs):
    for sample_input, expected_output in zip(inputs, outputs):
        actual_output = function(sample_input)
        try:
            assert actual_output == expected_output
        except AssertionError:
            print(
                (
                    "Something seems to be wrong with your code! On the input:\n{}\n"
                    "it should have returned:\n{}\nbut returned:\n{}\n instead!"
                ).format(sample_input, expected_output, actual_output)
            )



sample_input = r"""
This is some Downmark text. Note that *this* is in italic, and %this% is in bold.
If you want to write an \* or an equal sign and not have the parser eat them, 
that's easy -  note that \* this \* is not in italic even though it's between two \*s,
and \% this \% is not in bold.

[here](www.google.com) is a hyperlink.
[here](http://www.google.com) is another.
[and here](https://www.weird?$|site.weird/path/) is a third with some weird characters.
Follow it at your own peril.

Ideally, it would be good if your hyperlinks can contain parentheses and underscores.
But don't worry too much if some weird combination is ambiguous or results in
weird stuff.
"""

    




expected_output = r"""
This is some Downmark text. Note that <i>this</i> is in italic, and <b>this</b> is in bold.
If you want to write an \* or an equal sign and not have the parser eat them, 
that's easy -  note that \* this \* is not in italic even though it's between two \*s,
and \% this \% is not in bold.

<a href='http://www.google.com'>here</a> is a hyperlink.
<a href='http://www.google.com'>here</a> is another.
<a href='http://www.weird?$|site.weird/path/'>and here</a> is a third with some weird characters.
Follow it at your own peril.

Ideally, it would be good if your hyperlinks can contain parentheses and underscores.
But don't worry too much if some weird combination is ambiguous or results in
weird stuff.
"""
verify(parse_nwodkram, [sample_input], [expected_output])
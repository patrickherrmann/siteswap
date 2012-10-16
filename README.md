Siteswap Generator
==================

My first python script-- a ground state siteswap generator.

Constraints
-----------

Constraints can be passed as command line args in the order below.
Exclude argument is simply a list of integers of at least 0 length.

props - The number of objects to juggle.
maxheight - The highest throw to allow.
maxlength - The longest length pattern to generate.
exclude - An array of throw heights to avoid when generating the pattern.

Sample Run
----------
<pre>
python siteswap.py 4 6 5 0

4
53
552
5551
55613
5623
56252
5641
56612
633
6352
63551
63623
63641
642
6451
64613
6622
66251
6631
66611
</pre>
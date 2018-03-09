# Pi Day

This is a (soon to be organized) collection of code that I've written over the years for comuting pi in various languages and methods. These are all designed to be short so that I could embed them into tweets and facebook posts.

Here's one for comuting Pi in Perl.

    perl -e '$pi=0;for(0..1000000){$pi+=(4.0/($_*4.0+1))-(4.0/($_*4.0+3))}print "$pi\n"'


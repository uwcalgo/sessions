### A stab at scala
Scala solution to Greedy Gift Givers problem (http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=55).

The solution is implemented as a set of iterators (ProblemIterator and SolutionIterator). SolutionIterator is purely functional
(no *var* in sight!) and operates by transforming the input problem solution into a set of transactions (name, amount) which 
are then collected used *groupBy* and summed. This is my first attempt at coding in Scale so beware!

Note that the code can be parallelised by simply applying *par* to use the parallel version of various collections, e.g.

    val amounts_list = (problem.field_sets map

in SolutionIterator line 12 becomes

    val amounts_list = (problem.field_sets.par.map

as described in the [Scala documentation on parallel collections](http://docs.scala-lang.org/overviews/parallel-collections/overview.html).

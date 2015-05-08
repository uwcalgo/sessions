package greedygiftgivers

/**
 * Given a set of lines from a file defining Greedy Gift Givers problems,
 * iterate through the list of lines and return problems (type Problem).
 */
class ProblemIterator(lines : List[String]) extends Iterator[Problem] {
  var startingLine = 0
  def hasNext: Boolean = {startingLine < lines.length-1}
  def next: Problem = {
    val num_people = lines(startingLine).toInt
    val people = lines(startingLine+1).split("\\s").toList
    val end = startingLine + 2 + num_people
    val field_sets = lines.slice(startingLine+2, end) map {
      line => line.split("\\s").toList
    }
    startingLine = end
    new Problem(num_people, people, field_sets)}
}
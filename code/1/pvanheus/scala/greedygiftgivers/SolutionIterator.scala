package greedygiftgivers

/**
 * Iterator across a set of problems and provide solutions (as Lists of (name, amount) tuples)
 */
class SolutionIterator(lines: List[String]) extends Iterator[List[(String, Int)]] {
  val problem_iter = new ProblemIterator(lines)
  def hasNext: Boolean = { problem_iter.hasNext }
  def next: List[(String,Int)] = {
    val problem = problem_iter.next

    val amounts_list = (problem.field_sets map
      { case fields => List( (fields.head, -fields(1).toInt) ) :::
        fields.slice(3, fields.length).map {
          case name: String => (name, if (fields(2).toInt == 0) 0
                              else fields(1).toInt / fields(2).toInt) } }).flatten
    val results_map = amounts_list.groupBy(_._1) map { x => (x._1, (for (t <- x._2) yield t._2).sum) }
    problem.people map { name => (name, results_map.get(name).get) }
  }
}

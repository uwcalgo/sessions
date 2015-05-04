package greedygiftgivers

/**
 * Created by pvh on 2015/05/04.
 */
object Main {
  def main(args: Array[String]): Unit = {
    if (args.length != 1)
      Console.err.println("Usage: greedygiftgivers <data file>")
    else {
      // sample data "/home/pvh/IdeaProjects/GreedyGivers/data.txt"
      val source = scala.io.Source.fromFile(args(0))
      val lines = source.getLines.toList
      val solutions_iter = new SolutionIterator(lines)
      solutions_iter foreach (solution => {
        solution foreach(pair => println(pair._1 + " " + pair._2))
        println()
      })
    }
  }
}

package marching_band

/**
 * Created by pvh on 2015/05/12.
 */
object BandSolver {
  def main(args: Array[String]): Unit = {
    val parser = new BandParser(scala.io.Source.stdin.getLines())
    parser.parse()
  }
}

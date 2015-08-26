package marching_band

/**
 * Created by pvh on 2015/05/12.
 */
object BandParser {
  private def toTupleInt(line: String) = {
    line.split(" ") match {
      case fields: Array[String] => (fields(1).toInt, fields(2).toInt)
    }
  }
  private def toSingleInt(line: String) = {
    line.split(" ") match {
      case fields: Array[String] => fields(1).toInt
    }
  }

  def parse_case(lines: Iterator[String], r: Int, c: Int, n: Int): Unit = {
    var band = new Band(r, c)
    (1 to n) foreach { _ => lines.next() match {
      case line => line(0) match {
        case 'r' => {
          val (r1, r2) = toTupleInt(line)
          band = band.swap_rows(r1, r2)
        }
        case 'c' => {
          val (c1, c2) = toTupleInt(line)
          band = band.swap_rows(c1, c2)
        }
        case 'R' => band = band.reverse_rows
        case 'C' => band = band.reverse_columns
        case 'T' => band = band.transpose
        case 'V' => {
          val (x, y) = toTupleInt(line)
          println(band.at(x, y))
        }
        case 'P' => {
          val num = toSingleInt(line)
          val pos = band.find(num)
          println("%d %d".format(pos._1, pos._2))
        }
      }
    }}
  }
}

class BandParser(lines: Iterator[String]) {
  val test_cases = lines.next().toInt

  def parse() {
    (1 to test_cases) foreach { case_num => {
        println("Case #%d:".format(case_num))
        val (r, c, n) = lines.next().split(" ") match {
          case fields: Array[String] => (fields(0).toInt, fields(1).toInt, fields(2).toInt)
        }
        BandParser.parse_case(lines, r, c, n)
      }
    }
  }
}

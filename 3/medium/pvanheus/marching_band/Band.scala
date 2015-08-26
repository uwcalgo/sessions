package marching_band

/**
 * Created by pvh on 2015/05/12.
 */
class Band(r: Int, c: Int, init_matrix: Vector[Vector[Int]] = Vector(Vector()),
           init_transformations: List[(Int, Int) => (Int, Int)] = List(),
           init_r: Int = 0,
           init_c: Int = 0) {

  val init_rows = if (init_r == 0) r else init_r
  val init_cols = if (init_r == 0) c else init_c
  val matrix = if (init_matrix == Vector(Vector()))
    (1 to r map { x => (1 to c map { y => ((x-1)*c) + y }).toVector }).toVector
  else
    init_matrix
  val transformations = init_transformations

  def at(x: Int, y: Int) = { matrix(x-1)(y-1) }

  def find_helper(x: Int, y: Int,
                  t: List[(Int, Int) => (Int, Int)]): (Int, Int) = t match {
    case List() => (x,y)
    case _ => {
      val new_pos = t.head(x, y)
      find_helper(new_pos._1, new_pos._2, t.tail)
    }
  }

  def find(member: Int) = {
    val init_row = ((member - 1)/ init_cols) + 1
    val init_column = ((member - 1) % init_cols) + 1
    find_helper(init_row, init_column, transformations)
  }

  def reverse_columns() = {
    val new_matrix = (matrix map { row: Vector[Int] => row.reverse.toVector }).toVector
    new Band(r, c, new_matrix, transformations :+ ((x: Int, y: Int) => (x,c-y+1)))
  }

  def reverse_rows() = {
    val new_matrix = (r to 1 by -1 map { r => matrix(r-1) }).toVector
    new Band(r, c, new_matrix, transformations :+ ((x: Int, y: Int) => (r-x+1, y)))
  }

  def swap_rows(r1: Int, r2: Int) = {
    val new_matrix = (1 to r map {
      case `r1` => matrix(r2 - 1)
      case `r2` => matrix(r1 - 1)
      case num => matrix(num - 1)
    }).toVector
    new Band(r, c, new_matrix, transformations :+ (
      (x: Int, y: Int) => x match {
        case `r1` => (r2, y)
        case `r2` => (r1, y)
        case _ => (x, y)
      }))
  }

  def swap_columns(c1: Int, c2: Int) = {
    val new_matrix = (1 to r map {
      row_num => {
        (1 to c map {
          case `c1` => matrix(row_num - 1)(c2 - 1)
          case `c2` => matrix(row_num - 1)(c1 - 1)
          case col_num => matrix(row_num - 1)(col_num - 1)
        }).toVector
      }
    }).toVector
    new Band(r, c, new_matrix, transformations :+ (
      (x: Int, y: Int) => y match {
        case `c1` => (x, c2)
        case `c2` => (x, c1)
        case _ => (x,y)
      }))
  }

  def transpose() = {
    new Band(c, r, matrix.transpose, transformations :+ ((x: Int, y: Int) => { (y, x) }), r, c )
  }

  override def toString = {
    val width = scala.math.log10(r*c).toInt
    val format_str = "%" + (if (width > 0) width.toString else "") + "d"
    matrix map {
      case row => (row map { case num => format_str format num }) mkString " "
    } mkString "\n"
  }
}

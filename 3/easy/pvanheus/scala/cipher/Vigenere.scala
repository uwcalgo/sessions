package cipher

/**
 * Created by pvh on 2015/05/13.
 */
object Vigenere {

  def get_offset(c: Char): Int = if (c.isUpper) 65 else 97

  def encrypt_char(c: Char, key: Int): Char = {
    val offset = get_offset(c)
    (((c.toInt - offset + key) % 26) + offset).toChar
  }

  def decrypt_char(c: Char, key: Int): Char = {
    val offset = get_offset(c)
    val char_ordinal = if ((c.toInt - offset) < key) (c.toInt - offset - key + 26) else (c.toInt - offset - key)
    ((char_ordinal % 26) + offset).toChar
  }

  def make_key_array(key: String): Array[Int] = (key map { c => c.toInt - get_offset(c)}).toArray

  def vigenere(message: String, key: String, op: (Char, Int) => Char): String = {
    val key_array = make_key_array(key)
    val key_array_length = key_array.length
    def encrypt_vigenere_helper(message: String, keypos: Int, ciphertext: String): String = message match {
      case message if message.length == 0 => ciphertext
      case _ => message(0) match {
        case c if ! c.isLetter => encrypt_vigenere_helper(message.tail, keypos, ciphertext + c)
        case c => encrypt_vigenere_helper(message.tail, (keypos + 1) % key_array_length,  ciphertext + op(c, key_array(keypos)))
      }
    }
    encrypt_vigenere_helper(message, 0, "")
  }

  val encrypt_vigenere = (message: String, key: String) => vigenere(message, key, encrypt_char)
  val decrypt_vigenere = (message: String, key: String) => vigenere(message, key, decrypt_char)

  def main(args: Array[String]): Unit = {
    val message = scala.io.StdIn.readLine().stripLineEnd
    val key = scala.io.StdIn.readLine().stripLineEnd
    val encrypted = encrypt_vigenere(message, key)
    println(encrypted)
  }
}

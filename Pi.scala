object Pi {
    def main(args: Array[String]) {
        val pi = (0 to 1000000 by 2).toList.map(k => (4.0/(2.0 * k+1.0)) - (4.0/(2.0*k+3.0))).reduceLeft[Double](_+_)
        println(pi)
    }
}

using System;
using System.Collections.Generic;
using System.Text;

namespace cs
{ 
    public static class a119
    {
        private static Dictionary<string, float> mLog;

        public static void go()
        {
            string[] lines = read(@"'.\..\..\..\119\test.txt");

            bool numPeople = false;
            int x = -1; //number of people
            int y = -1; //person index
            bool byPeople = false;
            bool people = false;

            foreach(string line in lines)
            {
                string trim = line.Trim();

                if (!byPeople)
                {
                    if (trim.Length == 0)
                        continue;

                    if (!numPeople)
                    {
                        if (int.TryParse(trim, out x) && x != -1)
                        {
                            numPeople = true;
                            continue;
                        }
                    }
                    
                    else if (y == -1)
                    {
                        string[] peeps = trim.Split(' ');
                        mLog = new Dictionary<string, float>();

                        foreach (string peep in peeps)
                        {
                            mLog.Add(peep, 0.0f);
                        }

                        ++y;
                        byPeople = true;
                        continue;
                    }
                }

                ++y;                

                string[] data = trim.Split(' ');
                string from = data[0];
                int amount = int.Parse(data[1]);
                int split = int.Parse(data[2]);

                if (amount != 0 && split != 0 )
                {
                    take(from, amount);
                    float splitAmount = (amount * 1.0f) / split;
                    int len = data.Length;

                    for (int i = 3; i < len; i++)
                    {
                        give(data[i], splitAmount);
                    }
                }                                                    

                if (y == x)
                {
                    y = -1;
                    x = -1;
                    numPeople = false;
                    byPeople = false;
                    people = false;
                    print();
                }
                
            }

            System.Console.Read();
        }

        private static void print()
        {
            foreach(KeyValuePair<string, float> kvp in mLog)
            {
                System.Console.WriteLine(kvp.Key + " " + kvp.Value);
            }

            System.Console.WriteLine();
        }

        private static void take(string from, float amount)
        {
            mLog[from] -= amount;
        }

        private static void give(string to, float amount)
        {
            mLog[to] += amount;
        }

        private static string[] read(string path)
        {
            string[] lines = System.IO.File.ReadAllLines(path);
            return lines;
        }

    }
}

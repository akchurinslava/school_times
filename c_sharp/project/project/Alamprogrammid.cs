using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace project
{
	class Alamprogrammid
	{
		public static Double Eval(String expression)
		{
			System.Data.DataTable dataTable = new System.Data.DataTable();
			return Convert.ToDouble(dataTable.Compute(expression, String.Empty));

		}
        public static double Kalkulaator(double arv1, string tehe, double arv2)
		{
			double vastus = 0;
			if (tehe == "+")
			{
				vastus = arv1 + arv2;
			}
			else if(tehe == "-")
			{
				vastus = arv1 - arv2;
			}
			else if (tehe == "/")
			{
				try
				{
					vastus = arv1 / arv2;

				}
				catch (Exception exc)
				{
					Console.WriteLine(exc.Message);
				}
			}
			return vastus;
		}

    }
}
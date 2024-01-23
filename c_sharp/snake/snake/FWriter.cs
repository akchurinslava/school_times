using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Snake
{
	public class FWriter
	{
		string name;

		public void WriteNameToFile(string name, int score)
		{
			using (StreamWriter writer = File.AppendText("/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/c-/snake/snake/resources/results.txt"))
			{
				writer.WriteLine(name + ' ' + score.ToString() + "p");
				writer.Close();
			}

			Console.WriteLine("Name is added");
		}
		public void ShowResults()
		{
			StreamReader from_file = new StreamReader("/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/c-/snake/snake/resources/results.txt");
			string text = from_file.ReadToEnd();
			Console.WriteLine(text);
			from_file.Close();

		}
	}
}


using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace mobile_app
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class WordleEesti : ContentPage
	{
		//InitializeComponent ();
		Grid gr;
		Label lbl, lbl_lives, lbl_scores;
		Button btn;
		Entry entry;
		Frame frame;
        string folderPath;
        string filename;
		int lives = 3;
		int scores = 0;
		List<char> entries_chars_list = new List<char>();
		List<char> wordle_random_word;


        public WordleEesti(string folderPath, string filename) //Here we defined passed arguments and can use it by "this."
		{
            this.folderPath = folderPath; //Here
            this.filename = filename; //And here
			List<string> wordle_array = File.ReadAllLines(Path.Combine(folderPath, filename)).ToList();
			Random rnd = new Random();
			int random_index = rnd.Next(0, wordle_array.Count); //Here we took random number(index) from wordle_array
			string selected_word = wordle_array[random_index]; //Here we selected word by previous random_index
			wordle_random_word = selected_word.ToList(); //Here we modified selected word into list
			int random_word_length = wordle_random_word.Count; //Here we defined that list length


			gr = new Grid
			{
				RowDefinitions = {
					new RowDefinition { Height = new GridLength(1, GridUnitType.Star) }, //0 Label
					new RowDefinition { Height = new GridLength(1, GridUnitType.Star) }, //1 Entry
					new RowDefinition { Height = new GridLength(1, GridUnitType.Star) }, //2 Submit
					new RowDefinition { Height = new GridLength(4, GridUnitType.Star) }, //3 Lives and Scores
				},
				ColumnDefinitions = new ColumnDefinitionCollection(), //Use the collection, because we don't know exact char number in word

				BackgroundColor = Color.Gray,

			};


            //These foreach created for showing lists content
            foreach (var symbl in wordle_random_word)
            {
                Console.WriteLine(symbl);
            }

            Console.WriteLine("");
            foreach (var symbl in wordle_array)
            {
                Console.WriteLine(symbl);
	        }


            lbl = new Label
			{
				Text = "WORDLE EESTI!",
				FontSize = 30,
                HorizontalTextAlignment = TextAlignment.Center,
                HorizontalOptions = LayoutOptions.CenterAndExpand,
                


            };
			gr.Children.Add(lbl, 0, 0);
			Grid.SetColumnSpan(lbl, random_word_length);
            

			lbl_lives = new Label
			{
				Text = "Lives: " + lives.ToString(),
				FontSize = 20,
				HorizontalTextAlignment = TextAlignment.Center,

			};
			gr.Children.Add(lbl_lives, 0, 2);
            

            lbl_scores = new Label
			{
				Text = "Your score: " + scores.ToString(),
				FontSize = 20,
				HorizontalTextAlignment = TextAlignment.Center,
			};
			gr.Children.Add(lbl_scores, random_word_length-1, 2);


			btn = new Button
			{
                Text = "SEND!",
                BackgroundColor = Color.Green,
                TextColor = Color.White,
                VerticalOptions = LayoutOptions.CenterAndExpand,
                Margin = new Thickness(10, 300, 10, 0),
                FontSize = Device.GetNamedSize(NamedSize.Small, typeof(Button)),

            };
			gr.Children.Add(btn, 0, 3);
			Grid.SetColumnSpan(btn, random_word_length);
            btn.Clicked += Btn_Clicked;


            //We used for, because we don't exactly know much entries needs
            for (int j = 0; j < random_word_length; j++)
            {
				entry = new Entry
				{
					
					MaxLength = 1,
					HorizontalTextAlignment = TextAlignment.Center,
					VerticalOptions = LayoutOptions.CenterAndExpand,
					Keyboard = Keyboard.Text,
					BackgroundColor = Color.Transparent,
                   

                };


                frame = new Frame
                {
                    BorderColor = Color.Black, 
                    Padding = new Thickness(5),
                    Content = entry,
					BackgroundColor = Color.Transparent,
                    Margin = new Thickness(3, 0, 3, 0),
                };

                gr.Children.Add(frame, j, 1); 
            }


            Content = gr;


        }

        private async void Btn_Clicked(object sender, EventArgs e)
        {
            //Here we used some not regular loop in order to catch values in entries
            foreach (var child in gr.Children)
            {
                if (Grid.GetRow(child) == 1 && child is Frame frame)
                {
                    if (frame.Content is Entry entry)
                    {
                        string entry_text = entry.Text;
                        
                        //We control doest entry_text not empty
                        if (!string.IsNullOrEmpty(entry_text))
                        {
                            entries_chars_list.AddRange(entry_text.ToLower().ToCharArray());
                            for (int i = 0; i < entries_chars_list.Count; i++)
                            {
                                if (entries_chars_list[i] == wordle_random_word[i]) //If char is correct and on the right place
                                {
                                    entry.BackgroundColor = Color.Green;
                                    frame.BackgroundColor = Color.Green;
                                    scores += 1;
                                    lbl_scores.Text = "Your score: " + scores.ToString();
                                   

                                }
                                
                                else if (wordle_random_word.Contains(entries_chars_list[i])) //If char contains in word, but not on right place
                                {
                                    entry.BackgroundColor = Color.Yellow;
                                    frame.BackgroundColor = Color.Yellow;

                                }
                                
                                else if (!wordle_random_word.Contains(entries_chars_list[i])) //If char is not correct
                                {
                                    entry.BackgroundColor = Color.Red;
                                    frame.BackgroundColor = Color.Red;
                                    scores -= 1;
                                    lbl_scores.Text = "Your score: " + scores.ToString();

                                }        

                            }

                        }
                    }
                }
            }

            
            lives -= 1;
            lbl_lives.Text = "Lives: " + lives.ToString();

            
            //Here we check does lives equal zero or not, if yes we finish game
            bool equal = entries_chars_list.SequenceEqual(wordle_random_word);
            if (lives == 0)
            {
                await DisplayAlert("GAME OVER!", "YOUR SCORE: " + scores.ToString(), "OK");
                
                await Navigation.PushAsync(new StartPage1());
	        }

            //If all chars are correct and on there places, player wins
            else if(equal)
            {
                await DisplayAlert("YO WIN!", "YOUR SCORE: " + scores.ToString(), "OK");

                await Navigation.PushAsync(new StartPage1());
            }	        


            entries_chars_list.Clear();

        }

    }


}


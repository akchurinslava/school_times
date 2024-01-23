using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace mobile_app
{
	[XamlCompilation(XamlCompilationOptions.Compile)]	
	
	public partial class WordleEestiNav : ContentPage
	{
		Grid gr;
		Entry entr;
		Button btn, btn_save, btn_delete;
		Label lbl;
        string folderPath = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData);
		string filename = "worlde_array";
        List<string> worlde_array_list = new List<string>();
		string filePath;
		string[] lines;


        public WordleEestiNav()
		{
            filePath = Path.Combine(folderPath, "worlde_array");
            lines = File.ReadAllLines(filePath);
            worlde_array_list.AddRange(lines);


            gr = new Grid
			{
				RowDefinitions =
				{
					new RowDefinition { Height = new GridLength(1, GridUnitType.Star) }, //0 Label
					new RowDefinition { Height = new GridLength(1, GridUnitType.Star) }, //1 Entry
					new RowDefinition { Height = new GridLength(1, GridUnitType.Star) }, //2 btn, btn_save, btn_delete
				},

				ColumnDefinitions =
				{
					new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) }, //0
					new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) }, //1
					new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) }, //2
				},

				BackgroundColor = Color.Gray,
			};


            //Foreach loop created for test
            foreach (var symbl in worlde_array_list)
            {
                Console.WriteLine(symbl);
            }


            lbl = new Label
			{
				Text = "Wordle Eesti Start Leht",
				FontSize = 30,
                HorizontalTextAlignment = TextAlignment.Center,
            };
			gr.Children.Add(lbl, 0, 0);
			Grid.SetColumnSpan(lbl, 3);


			entr = new Entry
			{
                Placeholder = "Sissesta sõna",
                HorizontalTextAlignment = TextAlignment.Center,	
            };
			gr.Children.Add(entr, 0, 1);
			Grid.SetColumnSpan(entr, 3);


			btn_save = new Button
			{
                Text = "Salvesta",
                BackgroundColor = Color.Green,
                TextColor = Color.White,
                VerticalOptions = LayoutOptions.CenterAndExpand,
                FontSize = Device.GetNamedSize(NamedSize.Small, typeof(Button)),
                
            };
			gr.Children.Add(btn_save, 0, 2);
            btn_save.Clicked += BtnSave_Clicked;


			btn_delete = new Button
			{
                Text = "Delete",
                BackgroundColor = Color.Green,
                TextColor = Color.White,
                VerticalOptions = LayoutOptions.CenterAndExpand,
                FontSize = Device.GetNamedSize(NamedSize.Small, typeof(Button)),
            };
			gr.Children.Add(btn_delete, 1, 2);
            btn_delete.Clicked += Btn_delete_Clicked;


			btn = new Button
			{
				Text = "GO!",
				BackgroundColor = Color.Green,
				TextColor = Color.White,
				VerticalOptions = LayoutOptions.CenterAndExpand,
				FontSize = Device.GetNamedSize(NamedSize.Small, typeof(Button)),
				
			};
			gr.Children.Add(btn, 2, 2);
            btn.Clicked += Btn_Clicked;


			Content = gr;
		}

        private void Btn_delete_Clicked(object sender, EventArgs e)
        {
			if(worlde_array_list.Contains(entr.Text))
			{
				worlde_array_list.Remove(entr.Text);
                File.WriteAllLines(filePath, worlde_array_list);
                entr.Text = string.Empty;

                //Foreach loop created for test
                foreach (var symbl in worlde_array_list)
                {
                    Console.WriteLine(symbl);
                }

            }
        }

        private async void Btn_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new WordleEesti(folderPath, filename)); //Here we passed the arguments(folderPath and filname)
        }

        async void BtnSave_Clicked(System.Object sender, System.EventArgs e)
        {
            if (worlde_array_list.Contains(entr.Text))
            {
                await DisplayAlert("OOPS!", "This word already in list ", "OK");
            }
            File.AppendAllText(Path.Combine(folderPath, filename), entr.Text + Environment.NewLine);
            entr.Text = string.Empty;

            //Foreach loop created for test
            foreach (var symbl in worlde_array_list)
            {
                Console.WriteLine(symbl);
            }

        }
    }
}


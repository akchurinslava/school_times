using System;
using System.Collections.Generic;
using System.IO;
using Xamarin.Forms;

namespace maakonnad
{	
	public partial class Maakonnad : ContentPage
	{
		
		bool edited = true;
		string filename;
		string folderPath = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData);
        public Maakond Maakond { get; set; }
		public Maakonnad (Maakond maakond)
		{
			
			InitializeComponent ();
            //BackgroundColor = Color.Gray;
            Maakond = maakond;
			if (maakond == null)
			{
				Maakond = new Maakond();
				edited = false;
			}
			this.BindingContext = Maakond;
		}

        async void Button_Clicked(System.Object sender, System.EventArgs e)
        {
			await Navigation.PopAsync();
			if (edited == false)
			{
				NavigationPage navPage = (NavigationPage)Application.Current.MainPage;
				IReadOnlyList<Page> navStack = navPage.Navigation.NavigationStack;
				MainPage homePage = navStack[navPage.Navigation.NavigationStack.Count - 1] as MainPage;
				if (homePage != null)
				{
					homePage.AddMaakond(Maakond);
				}
			}
        }

        async void Salvesta_failisse(object sender, EventArgs e)
        {
			filename = "Maakond.txt";
			if (String.IsNullOrEmpty(filename)) return;
			if (File.Exists(Path.Combine(folderPath, filename)))
			{
				bool isRewrited = await DisplayAlert("Kinnitus", "Fail on juba olemas, lisame andmeid sinna", "Jah", "Ei");
				if (isRewrited == false) return;
			}
			string text = nimetusEntry.Text +' ' +pealinnEntry.Text+ ' '+teineLinnEntry.Text + ' '+arv_stepper.Value.ToString()+ ' ' +arv_stepper2.Value.ToString()+ ' ' +arv_stepper3.Value.ToString();
			File.AppendAllLines(Path.Combine(folderPath, filename), text.Split('\n'));
        }

        private void Loe_failist(object sender, EventArgs e)
        {
			filename = "Maakond.txt";
			if (String.IsNullOrEmpty(filename)) return;
			if (filename != null)
			{
				lbl.Text = File.ReadAllText(Path.Combine(folderPath, filename));
			}

        }

        private void Kustutu_faili(object sender, EventArgs e)
        {
			File.Delete(Path.Combine(folderPath, filename));
        }
    }
}


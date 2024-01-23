using System;
using System.Collections.ObjectModel;
using System.IO;
using System.Linq;
using Xamarin.Forms;

namespace maakonnad
{
    public partial class MainPage : ContentPage
    {
        string filename;
        string folderPath = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData);
        




        protected internal ObservableCollection<Maakond> Maakonads { get; set; }

        public MainPage()
        {
            InitializeComponent();
            //BackgroundColor = Color.Gray;
            Maakonads = new ObservableCollection<Maakond>
            {
                
                new Maakond {Nimetus="Harjumaa", Pealinn="Tallinn", TeineLinn = "Maardu", InimesteArv=52000, Pindala = 4327, Elanikke = 638076 },
                new Maakond { Nimetus = "Tartumaa", Pealinn = "Tartu", TeineLinn = "Peipsiääre", InimesteArv = 3000, Pindala = 3349, Elanikke = 638076 },
                new Maakond { Nimetus = "Ida-Viirumaa", Pealinn = "Jõhvi", TeineLinn = "Kohtla-Jarve", InimesteArv = 4000, Pindala = 2974, Elanikke = 638076 },
            };


            list.BindingContext = Maakonads;

            filename = "Maakond.txt";

            if (String.IsNullOrEmpty(filename)) return;
            if (filename != null)
            {
                String[] Andmed = File.ReadAllLines(Path.Combine(folderPath, filename));
                for (int i = 0; i < Andmed.Length; i++)
                {
                    var columns = Andmed[i].Split(' ');
                    var maakond = new Maakond(columns[0], columns[1], columns[2], int.Parse(columns[3]), int.Parse(columns[4]), int.Parse(columns[5]));
                    if (Maakonads.Where(m => m.Nimetus == maakond.Nimetus).FirstOrDefault() == null)
                    {
                        Maakonads.Add(maakond);
                    }
                };
                list.BindingContext = Maakonads;

            }
        }

        


        private async void Button_Clicked(System.Object sender, System.EventArgs e)
        {
            await Navigation.PushAsync(new Maakonnad(null));
        }

        private async void  list_ItemSelected(System.Object sender, Xamarin.Forms.SelectedItemChangedEventArgs e)
        {
            Maakond selected = e.SelectedItem as Maakond;
            if (selected != null)
            {
                
                list.SelectedItem = null;
                await Navigation.PushAsync(new Maakonnad(selected));
            }
        }
        protected internal void AddMaakond(Maakond maakond)
	    {
            Maakonads.Add(maakond);
	    }

        private void Loe_failist(System.Object sender, System.EventArgs e)
        {
            filename = "Maakond.txt";
            if (String.IsNullOrEmpty(filename)) return;
            if (filename != null)
            {
                String[] Andmed = File.ReadAllLines(Path.Combine(folderPath, filename));
                for (int i = 0; i < Andmed.Length; i++)
                {
                    var columns = Andmed[i].Split(' ');
                    var maakond = new Maakond(columns[0], columns[1], columns[2], int.Parse(columns[3]), int.Parse(columns[4]), int.Parse(columns[5]));
                    if (Maakonads.Where(m => m.Nimetus == maakond.Nimetus).FirstOrDefault() == null)
                    {
                        Maakonads.Add(maakond);
		            }    
		        };
                list.BindingContext = Maakonads;
             
            }
        }
    }
}



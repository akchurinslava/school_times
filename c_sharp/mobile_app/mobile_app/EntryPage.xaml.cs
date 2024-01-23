using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Essentials;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace mobile_app
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class EntryPage : ContentPage
    {
        Editor editor;
        Label label, label2;
        public EntryPage()
        {   
            //we dont need now to initialize second page
            //InitializeComponent();

            editor = new Editor
            {
                Placeholder = "Sisesta siia tekst",
                BackgroundColor = Color.HotPink,
                TextColor = Color.White,

            };

            //editor.TextChanged += Editor_TextChanged;

            label2 = new Label
            {
                Text = Preferences.Get("key2", "ei ole veel key2"),
                HorizontalOptions = LayoutOptions.Start,
                VerticalOptions = LayoutOptions.Center,
                TextColor = Color.Black,
                BackgroundColor = Color.Blue
            };

            label = new Label
            {
                Text = "Pealkiri",
                HorizontalOptions = LayoutOptions.Start,
                VerticalOptions = LayoutOptions.Center,
                TextColor = Color.Black,
                BackgroundColor = Color.Blue
            };

            Button b = new Button
            {
                Text = "To Start Page",
                HorizontalOptions = LayoutOptions.Center,
                VerticalOptions = LayoutOptions.Center,
            };

            b.Clicked += B_Clicked;

            Button c = new Button
            {
                Text = "Salvesta omadus",
                HorizontalOptions = LayoutOptions.Center,
                VerticalOptions = LayoutOptions.Center,
            };
            c.Clicked += C_Clicked;

            Button d = new Button
            {
                Text = "Salvesta preferences",
                HorizontalOptions = LayoutOptions.Center,
                VerticalOptions = LayoutOptions.Center,
            };
            d.Clicked += D_Clicked;

            StackLayout st = new StackLayout
            {
                Orientation = StackOrientation.Vertical,
                Children = {label, label2, editor, b, c, d},
                BackgroundColor = Color.Bisque
            };

            Content = st;
        }

        private void D_Clicked(object sender, EventArgs e)
        {
            string value2 = editor.Text;
            Preferences.Set("key2", value2);
            label2.Text = value2;
        }

        private void C_Clicked(object sender, EventArgs e)
        {
            string value = editor.Text;
            App.Current.Properties.Remove("key");
            App.Current.Properties.Add("key", value);
            label.Text = (string)App.Current.Properties["key"];
        }

        protected override void OnAppearing()
        {
            object key = "";
            if (App.Current.Properties.TryGetValue("key", out key))
	        {
                label.Text = (string)App.Current.Properties["key"];
		 
	        };
            base.OnAppearing();
        }

        //private void Editor_TextChanged(object sender, TextChangedEventArgs e)
        //{
        //    int key = e.NewTextValue?.Count(c => c == 'A') ?? 0;
        //    label.Text = "A: "+key.ToString();
        //}

        private async void B_Clicked(object sender, EventArgs e)
        {
            await Navigation.PopAsync();
        }
    }
}
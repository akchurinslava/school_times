using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace mobile_app
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class ImagePage : ContentPage
    {
        Switch sw;
        Image img;
        public ImagePage()
        {
            //InitializeComponent ();
            img = new Image { Source = "coin.jpg" };
            var tap = new TapGestureRecognizer();
            tap.Tapped += Tap_Tapped;
            tap.NumberOfTapsRequired = 2;
            img.GestureRecognizers.Add(tap);
            sw = new Switch
            {
                IsToggled = true,
                VerticalOptions = LayoutOptions.FillAndExpand,
                HorizontalOptions = LayoutOptions.Center,


            };

            sw.Toggled += Sw_Toggled;
            Content = new StackLayout { Children = { sw, img } };
        }

        int taps = 0;
        private void Tap_Tapped(object sender, EventArgs e)
        {
            taps++;
            Image img = (Image)sender;
            if (taps % 2 == 0)
            {
                img.Source = "coin.jpg";
            }
            else
            {
                img.Source = "coind.jpeg";
            }
        }

        private void Sw_Toggled(object sender, ToggledEventArgs e)
        {
            if (e.Value)
            {
                img.IsVisible = true;
            }
            else
            {
                img.IsVisible = false;
            }
        }
    }
}


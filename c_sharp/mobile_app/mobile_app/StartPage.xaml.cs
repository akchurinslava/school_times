﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace mobile_app
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class StartPage : ContentPage
    {
        public StartPage()
        {
            //InitializeComponent();

            Button Ent_btn = new Button
            {
                Text = "Entry page",
                BackgroundColor = Color.Azure,
            };

            Button Time_btn = new Button
            {
                Text = "Timer page",
                BackgroundColor = Color.Azure,
            };

            Button BoxViewPage = new Button
            {
                Text = "Box View Page",
                BackgroundColor = Color.Azure,
            };

            StackLayout st = new StackLayout
            {
                Children = {Ent_btn, Time_btn, BoxViewPage},
                BackgroundColor = Color.Beige
            };

            Content = st;
            Ent_btn.Clicked += Ent_btn_Clicked;
            Time_btn.Clicked +=Time_btn_Clicked;
            BoxViewPage.Clicked +=BoxViewPage_Clicked;
        }

        private async void BoxViewPage_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new BoxViewPage());
        }

        private async void Time_btn_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new TimerPage());
        }

        private async void Ent_btn_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new EntryPage());
        }
    }
}
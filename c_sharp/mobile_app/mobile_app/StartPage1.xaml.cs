using System;
using System.Collections.Generic;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace mobile_app
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class StartPage1 : ContentPage
	{
		List<ContentPage> pages = new List<ContentPage>() { new EntryPage(), new BoxViewPage(), new TimerPage(), new DateTimePage(), new StepperSliderPage(), new TrafficLight(), new FrameGridPage(), new ImagePage(), new PickerPage(), new OwnBrowser(), new TablePage(), new FilePage(), new WordleEestiNav() };
		List<string> tekst = new List<string> { "Ava Entry leht", "Ava BoxView leht", "Ava Timer leht", "Ava DateTime leht", "Ava StepperSlider leht", "Ava TrafficLight leht", "Ava Grid leht", "Ava Image leht", "Ava Picker Page", "Ava OmaBrowswer", "Ava TablePage", "Ava FilePage", "Ava Worlde Eesti" };
		StackLayout st;
        public StartPage1 ()
		{
			//InitializeComponent ();
			st = new StackLayout
			{
				Orientation = StackOrientation.Vertical,
				BackgroundColor = Color.Gray
			};

			for (int i = 0; i < pages.Count; i++) 
			{
				Button button = new Button
				{
					Text = tekst[i],
					TabIndex = i,
                    BackgroundColor = Color.Green,
                    TextColor = Color.White,


                };
				st.Children.Add(button);
                button.Clicked += Button_Clicked;
				
			}
			ScrollView sv = new ScrollView { Content=st };
			Content = sv;
		}

        private async void Button_Clicked(object sender, EventArgs e)
        {
			Button btn = (Button)sender;
			await Navigation.PushAsync(pages[btn.TabIndex]);
        }
    }
}


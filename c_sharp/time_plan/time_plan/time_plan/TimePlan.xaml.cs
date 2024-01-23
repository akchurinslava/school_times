using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;


namespace time_plan
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class TimePlan : ContentPage
	{
        Label label;
		TimePicker time;
		Grid gr;
		Image img;
        Entry entr;
        StackLayout stk;
        Frame frame, frameForList;
        
        public TimePlan ()
		{
            //InitializeComponent ();
            gr = new Grid
			{
				RowDefinitions =
				{
					new RowDefinition { Height = new GridLength(1, GridUnitType.Star) }, //0
					new RowDefinition { Height = new GridLength(2, GridUnitType.Star) }, //1
					new RowDefinition { Height = new GridLength(1, GridUnitType.Star) },  //2
				},

				ColumnDefinitions =
				{
					new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) }, //0
					new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) }, //1
					new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) }, //2
				},

				BackgroundColor = Color.Gray,
			};

			label = new Label
			{
				Text = "VALI AEG",
                BackgroundColor = Color.Green,
                TextColor = Color.White,
                HorizontalOptions = LayoutOptions.CenterAndExpand,
                VerticalOptions = LayoutOptions.CenterAndExpand,
				FontAttributes = FontAttributes.Bold,
                FontSize = Device.GetNamedSize(NamedSize.Small, typeof(Label))
                //Margin = new Thickness(10, 20, 10, 0),
                //HorizontalOptions = LayoutOptions.FillAndExpand,
            };

            frame = new Frame
            {
                Content = label,
                BackgroundColor = Color.Green,
                CornerRadius = 30,
                Margin = new Thickness(10, 20, 10, 0),
            };
            gr.Children.Add(frame, 0, 0);
            Grid.SetColumnSpan(frame, 3);
			//Grid.SetRowSpan(frame, 1);



			time = new TimePicker
			{
				Time = new TimeSpan(0, 0, 0),
				Format = "HH:mm",
				BackgroundColor = Color.Transparent,
				TextColor = Color.Black,
				FontSize = 40,
			};
            gr.Children.Add(time, 0, 1);

            entr = new Entry 
	        {
                Placeholder = "Sisesta märge",
	        };
            gr.Children.Add(entr, 0, 3);
            entr.Completed += Entr_Completed;

            stk = new StackLayout

            {
                HorizontalOptions = LayoutOptions.CenterAndExpand,
                VerticalOptions = LayoutOptions.CenterAndExpand,
                Orientation = StackOrientation.Vertical,
                Spacing = 5
            };

            frameForList = new Frame
            {
                Content = stk,
                CornerRadius = 30,
                BackgroundColor = Color.Transparent,
                Margin = new Thickness(10, 20, 10, 0),
            };
            gr.Children.Add(frameForList, 1, 3);
            Grid.SetColumnSpan(frameForList, 2);


            Content = gr;

            time.PropertyChanged += Time_PropertyChanged;

			img = new Image { Source = "" };
            var tap = new TapGestureRecognizer();
            tap.Tapped += Tap_TappedAsync;
            tap.NumberOfTapsRequired = 2;
            img.GestureRecognizers.Add(tap);
            gr.Children.Add(img, 1, 1);
			Grid.SetColumnSpan(img, 2);

        }

        private void Entr_Completed(object sender, EventArgs e)
        {
            TimeSpan selectedTime = time.Time;
            string entrText = entr.Text;
            if (!string.IsNullOrWhiteSpace(entrText))
            {
                
                var label = new Label
                {
                    Text = selectedTime.ToString("hh\\:mm") +" "+entrText,
                    FontSize = 16,
                    TextColor = Color.Black
                };

                
                stk.Children.Add(label);

                
                entr.Text = string.Empty;
            }

        }

        private async void Tap_TappedAsync(object sender, EventArgs e)
        {
            await DisplayAlert("Hoiatus", "Ära kliiki pildi peale!", "OK");
        }

        private void Time_PropertyChanged(object sender, System.ComponentModel.PropertyChangedEventArgs e)
		{
			if (e.PropertyName == TimePicker.TimeProperty.PropertyName)
			{
				UpdateImage();
			}
		}

        private void UpdateImage()
        {
			TimeSpan selectedTime = time.Time;
			if (selectedTime.Hours == 12)
			{
                img.Source = "Day.png";
				label.Text = "Pragu on päev";
            }
			else if (selectedTime.Hours == 15)
			{
                img.Source = "PictureMorning.png";
                label.Text = "Pragu on keset päeva";
            }
            else if (selectedTime.Hours == 18)
            {
                img.Source = "EarlyEvening.png";
                label.Text = "Pragu on varajane õhtu";
            }
            else if (selectedTime.Hours == 20)
            {
                img.Source = "PictureEvening.png";
                label.Text = "Pragu on hilisõhtul";
            }
            else if (selectedTime.Hours == 23)
            {
                img.Source = "LaterEvening.png";
                label.Text = "Pragu on peaaegu öö";
            }
            else if (selectedTime.Hours == 24)
            {
                img.Source = "MidNight.png";
                label.Text = "Pragu on keset öö";
            }
            else if (selectedTime.Hours == 1)
            {
                img.Source = "EarlyNightpng";
                label.Text = "Pragu on varjane öö";
            }
            else if (selectedTime.Hours == 5)
            {
                img.Source = "LaterNight.png";
                label.Text = "Pragu on hilisöö";
            }
            else if (selectedTime.Hours == 3)
            {
                img.Source = "Night.png";
                label.Text = "Pragu on öö";
            }
            else if (selectedTime.Hours == 4)
            {
                img.Source = "PictureNight.png";
                label.Text = "Pragu on teine öö osa";
            }
            else if (selectedTime.Hours == 6)
            {
                img.Source = "EarlyEvening.png";
                label.Text = "Pragu on varjane hommik";
            }
            else if (selectedTime.Hours == 9)
            {
                img.Source = "Evening.png";
                label.Text = "Pragu on hommik";
            }
            else
	        {
                img.Source = "";
                label.Text = "VALI TEINE AEG";
            }
        }
    }
}


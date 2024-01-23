using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace time_plan
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class MainPage : ContentPage
    {
        List<ContentPage> pages = new List<ContentPage> { new TimePlan() };
        List<string> text_label = new List<string> { "Ava ajaplaani leht" };
        StackLayout st;
        public MainPage()
        {
            //InitializeComponent();
            st = new StackLayout
            {
                Orientation = StackOrientation.Vertical,
                BackgroundColor = Color.Gray

            };

            for (int i = 0; i < pages.Count; i++)
            {
                Button button = new Button
                {
                    Text = text_label[i],
                    TabIndex = i,
                    BackgroundColor = Color.Green,
                    TextColor = Color.White,
                    HorizontalOptions = LayoutOptions.CenterAndExpand,
		            VerticalOptions = LayoutOptions.CenterAndExpand,
		            FontSize = Device.GetNamedSize(NamedSize.Small, typeof(Button)) 
                    
                };
                st.Children.Add(button);
                button.Clicked += Button_Clicked;
            }
            ScrollView sv = new ScrollView { Content = st };
            Content = sv;
        }

        private async void Button_Clicked(object sender, EventArgs e)
        {
            Button btn = (Button)sender;
            await Navigation.PushAsync(pages[btn.TabIndex]);
        }
    }
}

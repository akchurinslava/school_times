using System;
using System.Collections.Generic;
using Plugin.Messaging;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace mobile_app
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class TablePage : ContentPage
	{
        TableView tableView;
		SwitchCell switchCell;
		ImageCell imageCell;
		TableSection fotoSection;
        EntryCell name = new EntryCell { Label = "nimi.: ", Placeholder = "Kirjuta oma nimi", Keyboard = Keyboard.Default };
        EntryCell tel = new EntryCell { Label = "tel.:", Placeholder = "Kirjuta oma tel. nr. ", Keyboard = Keyboard.Telephone };
        EntryCell smes = new EntryCell { Label = "SMS:", Placeholder = "Sisesta oma SMSi", Keyboard = Keyboard.Text };
        EntryCell email = new EntryCell { Label = "mail:", Placeholder = "Kirjuta oma mail", Keyboard = Keyboard.Email };
		Editor ed = new Editor { Placeholder = "Enter your mail message:", Keyboard = Keyboard.Default, AutoSize = EditorAutoSizeOption.TextChanges, HorizontalOptions = LayoutOptions.FillAndExpand };
        //ViewCell viewCell;


        public TablePage()
		{
			//InitializeComponent ();

			fotoSection = new TableSection();
			switchCell = new SwitchCell { Text = "Näita" };
            switchCell.OnChanged += SwitchCell_OnChanged;
			imageCell = new ImageCell { Text = "Foto:", ImageSource="coin.png", Detail="Kirjeldus" };
			Button callButton = new Button { Text = "Call" };
            callButton.Clicked += CallButton_Clicked;
			Button smsButton = new Button { Text = "SMS" };
            smsButton.Clicked += SmsButton_Clicked;
			Button mailButton = new Button { Text = "MAIL" };
            mailButton.Clicked += MailButton_Clicked;

			tableView = new TableView
			{
				Intent = TableIntent.Form,
				Root = new TableRoot("Andmed:")
				{
					new TableSection("Põhi andmed:")
					{
						name
					},

					new TableSection("Kontakti andmed:")
					{

						tel,
						email,
						smes,
						switchCell
					},

					fotoSection,

					new TableSection("Actions")
					{
						new ViewCell
						{
							View = new StackLayout
							{
								Orientation = StackOrientation.Vertical,
								Children =
								{
									callButton
								}

							}


						},
						new ViewCell
						{
							View = new StackLayout
							{
								Orientation = StackOrientation.Vertical,
								Children =
								{
									smsButton
								}

							}


						},

						new ViewCell
						{
							View = new StackLayout
							{
								Orientation = StackOrientation.Vertical,
								Children =
								{
									mailButton
								}

							}


						},
						new ViewCell
						{
							View = new StackLayout
							{
								Orientation = StackOrientation.Vertical,
								Children =
								{
									ed
                                }

                            }


                        },


                    }
					
				}
				
			};
            
			
			Content = tableView;
		}

        private void MailButton_Clicked(object sender, EventArgs e)
        {
			var mail = CrossMessaging.Current.EmailMessenger;
			if (mail.CanSendEmail)
			{
				mail.SendEmail(email.Text, "Hello World!", ed.Text);
			}
        }

        private void SmsButton_Clicked(object sender, EventArgs e)
        {
			var sms = CrossMessaging.Current.SmsMessenger;
			if (sms.CanSendSms)
			{
				sms.SendSms(tel.Text, smes.Text);
			}
        }

        private void CallButton_Clicked(object sender, EventArgs e)
        {
            var call = CrossMessaging.Current.PhoneDialer;
            if (call.CanMakePhoneCall)
            {
                call.MakePhoneCall(tel.Text);
            }
        }

        private void SwitchCell_OnChanged(object sender, ToggledEventArgs e)
        {
            if (e.Value) //short version of e.Value == true
			{
				fotoSection.Title = "Foto: ";
				fotoSection.Add(imageCell);
				switchCell.Text = "Peida";
			}
			else
			{
				fotoSection.Title = "";
				fotoSection.Remove(imageCell);
				switchCell.Text = "Naita";
			}
        }
    }
}


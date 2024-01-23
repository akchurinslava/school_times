using System;
using System.ComponentModel;
using System.Drawing;

namespace maakonnad
{
	public class Maakond: INotifyPropertyChanged
	{
		string nimetus;
		string pealinn;
        string teineLinn;
		int inimesteArv;
        int pindala;
        int elanikke;



        public Maakond() { }

        public Maakond(string Nimetus, string Pealinn, string Teine_linn, int Inimeste_arv, int Pindala, int Elanikke)
	    {
            
            nimetus = Nimetus;
            pealinn = Pealinn;
            teineLinn = Teine_linn;
            inimesteArv = Inimeste_arv;
            pindala = Pindala;
            elanikke = Elanikke;



	    }

		public string Nimetus
		{
			get { return nimetus; }
			set
			{ 
				if (nimetus != value)
				{
					nimetus = value;
					OnPropertyChanged("Nimetus");

				}
			}
		}
        public string Pealinn
        {
            get { return pealinn; }
            set
            {
                if (pealinn != value)
                {
                    pealinn = value;
                    OnPropertyChanged("Pealinn");

                }
            }
        }
        public string TeineLinn
        {
            get { return teineLinn; }
            set
            {
                if (teineLinn != value)
                {
                    teineLinn = value;
                    OnPropertyChanged("TeineLinn");

                }
            }
        }
        public int InimesteArv
        {
            get { return inimesteArv; }
            set
            {
                if (inimesteArv != value)
                {
                    inimesteArv = value;
                    OnPropertyChanged("InimesteArv");

                }
            }
        }

        public int Pindala
        {
            get { return pindala; }
            set
            {
                
                if (pindala != value)
                {
                    pindala = value;
                    OnPropertyChanged("Pindala");

                }
            }
        }

        public int Elanikke
        {
            get { return elanikke; }
            set
            {
                
                if (elanikke != value)
                {
                    elanikke = value;
                    OnPropertyChanged("Elanikke");

                }
            }
        }


        private void OnPropertyChanged(string v="")
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(v));
        }

        public event PropertyChangedEventHandler PropertyChanged;
    }
    
}





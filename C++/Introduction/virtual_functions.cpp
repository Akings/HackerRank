class Person{
  public:
    string name;
    int age;
    virtual void getdata(){}
    virtual void putdata(){}
};

class Professor:public Person{
  public:
    int publications,id1;
    static int cur_id1;
    virtual void getdata(){
      cur_id1++;
      cin >> name;
      cin >> age;
      cin >> publications;
      id1 = cur_id1;
    }
    virtual void putdata(){
          cout << name << " " << age << " " << publications << " " << id1 << "\n";
    }
};int Professor::cur_id1=0;

class Student:public Person{
  public:
    int marks[6];
    static int cur_id;
    int sum=0,id;
    virtual void getdata(){
    	cur_id++;
      cin>>name>>age;
      for(int i=0;i<6;i++){
        cin>>marks[i];
        sum+=marks[i];
        id=cur_id;
      }
    }
    virtual void putdata(){
      cout<<name<<" "<<age<<" "<<sum<<" "<<id<<endl;
    }
};int Student::cur_id=0;

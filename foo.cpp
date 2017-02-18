#include <iostream>
#include <ctime>

class Foo{
    public:
        void bar(){
	  std::cout << time(0) << " c++ begin cpu bound: " << std::endl;
	  clock_t begin = std::clock();
	  int a = 0;
	  for (int i = 0; i < 1000000000 / 1.86; i++) {
	    a = i;
	  }
	  clock_t end = std::clock();
	  double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	  std::cout << time(0) << " c++ elapsed time: " << elapsed_secs << std::endl;
        }
};

extern "C" {
    Foo* Foo_new(){ return new Foo(); }
    void Foo_bar(Foo* foo){ foo->bar(); }
}

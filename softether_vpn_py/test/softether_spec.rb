control 'softether' do
    impact 1.0
    title 'Проверка работы SoftEther'
    desc 'Убедитесь, что SoftEther запущен и работает на целевой системе'
  
    describe service('softether') do
      it { should be_running }
      it { should be_enabled }
    end
  
    describe port(443) do
      it { should be_listening }
    end
  end
Rails.application.routes.draw do
  get 'plotter/main'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root to: 'plotter#main' 
end

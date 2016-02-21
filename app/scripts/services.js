'use strict';

angular.module('confusionApp')
        .constant("baseURL","http://localhost:3000/")
       .service('menuFactory', ['$resource', 'baseURL', function($resource,baseURL) {
    
         
            this.getDishes = function(){
                                        return $resource(baseURL+"dishes/:id",null,  {'update':{method:'PUT' }});
                                    };
               this.getJob = function(){
                                        return $resource(baseURL+"cisco/:id",null,  {'update':{method:'PUT' }});
                                    };
         
    
           this.getPromotion = function(){
                                        return  $resource(baseURL+"promotions/:id",null);
                                    };
           
    
                        
        }])

        .factory('corporateFactory', ['$resource', 'baseURL', function($resource,baseURL) {
    
           var corpfac = {};

           corpfac.getLeaders = function() {

                return $resource(baseURL+"leadership/:id",null, {'update':{method:'PUT' }});
           };
            return corpfac;
    
        }])


    .factory('jobFactory', ['$resource', 'baseURL', function($resource,baseURL) {
    
           var jobfac = {};

           jobfac.getJobs = function() {

                return $resource(baseURL+"cisco/:id",null, {'update':{method:'PUT' }});
           };
            return jobfac;
    
        }])

        .service('feedbackFactory', ['$resource', 'baseURL', function($resource,baseURL) {  
            
            this.getFeedback = function(){                        
       
                return $resource(baseURL+"feedback/:firstName",null, {'save':{method:'POST' }});                    
            };                    
        }])

    ;

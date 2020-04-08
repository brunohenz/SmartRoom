using System;
using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using API.Models;

namespace API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UserController : ControllerBase
    {        
        [HttpGet("{cpf}")]
        public User Get(string CPF)
        {
            return new User { IdUser = 1, Nome = "Bruno Henrique Salomão", CPF = "33197124898"};
        }
    }
}
